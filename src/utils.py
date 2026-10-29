import numpy as np

INCONEL_718_PROPS = {'X_T': 965.0, 'X_C': 1100.0, 'Y_T': 860.0, 'Y_C': 980.0, 'S_13': 550.0}

def compute_tsai_wu_coefficients(props=None):
    p = props or INCONEL_718_PROPS
    X_T, X_C = p['X_T'], p['X_C']
    Y_T, Y_C = p['Y_T'], p['Y_C']
    S_13 = p['S_13']
    return {
        'F_1': (1.0 / X_T) - (1.0 / X_C),
        'F_11': 1.0 / (X_T * X_C),
        'F_2': (1.0 / Y_T) - (1.0 / Y_C),
        'F_22': 1.0 / (Y_T * Y_C),
        'F_66': 1.0 / (S_13**2),
        'F_12': -0.5 * np.sqrt((1.0 / (X_T * X_C)) * (1.0 / (Y_T * Y_C)))
    }

def evaluate_failure_index(sigma_1, sigma_2, tau_13, coeffs=None):
    c = coeffs or compute_tsai_wu_coefficients()
    return (c['F_1']*sigma_1 + c['F_2']*sigma_2 + c['F_11']*(sigma_1**2) + c['F_22']*(sigma_2**2) + 2.0*c['F_12']*sigma_1*sigma_2 + c['F_66']*(tau_13**2))

def solve_strength_reserve_ratio(sigma_1, sigma_2, tau_13, coeffs=None):
    c = coeffs or compute_tsai_wu_coefficients()
    A = c['F_11']*(sigma_1**2) + c['F_22']*(sigma_2**2) + 2.0*c['F_12']*sigma_1*sigma_2 + c['F_66']*(tau_13**2)
    B = c['F_1']*sigma_1 + c['F_2']*sigma_2
    if A <= 0: return float('inf')
    disc = B**2 + 4.0*A
    return (-B + np.sqrt(disc)) / (2.0*A) if disc >= 0 else float('nan')
