__all__ = [
    'ZieglerNichols',
    'CohenCoon',
    'ChienHronesReswick0',
    'ChienHronesReswick20',
]


def ZieglerNichols(g, sample_time, total_time, n_method):
    
    t, y = n_method(g, sample_time, total_time)
    
    k = y[-1]
    
    t63 = get_time_near(t, y, 0.632*k)
    t28 = get_time_near(t, y, 0.28*k)
    tau = 1.5*(t63-t28)
    L = 1.5*(t28-(t63/3))
    
    kp = (1.2*tau)/(k*L)
    Ti = 2*L
    Td = L/2
    
    ki = kp/Ti
    kd = kp*Td
    
    return kp, ki, kd


def CohenCoon(g, sample_time, total_time, n_method):
    
    t, y = n_method(g, sample_time, total_time)
    
    k = y[-1]
    
    t63 = get_time_near(t, y, 0.632*k)
    t28 = get_time_near(t, y, 0.28*k)
    tau = 1.5*(t63-t28)
    L = 1.5*(t28-(t63/3))
    
    R = L/tau
    kp = tau/(k*L*((4/3)+(R/4)))
    Ti = L*((32 + 6*R)/(13 + 8*R))
    Td = 4/(13 + 8*R)
    
    ki = kp/Ti
    kd = kp*Td
    
    return kp, ki, kd


def ChienHronesReswick0(g, sample_time, total_time, n_method):
    
    t, y = n_method(g, sample_time, total_time)
    
    k = y[-1]
    
    t63 = get_time_near(t, y, 0.632*k)
    t28 = get_time_near(t, y, 0.28*k)
    tau = 1.5*(t63-t28)
    L = 1.5*(t28-(t63/3))
    
    kp = (0.6*tau)/(k*L)
    Ti = tau
    Td = L/2
    
    ki = kp/Ti
    kd = kp*Td
    
    return kp, ki, kd


def ChienHronesReswick20(g, sample_time, total_time, n_method):
    
    t, y = n_method(g, sample_time, total_time)
    
    k = y[-1]
    
    t63 = get_time_near(t, y, 0.632*k)
    t28 = get_time_near(t, y, 0.28*k)
    tau = 1.5*(t63-t28)
    L = 1.5*(t28-(t63/3))
    
    kp = (0.95*tau)/(k*L)
    Ti = 1.4*tau
    Td = 0.47*L
    
    ki = kp/Ti
    kd = kp*Td
    
    return kp, ki, kd


def get_time_near(t, y, point):
    
    tolerance_range = max(y) - min(y)
    
    for i in range(len(y)):
        
        tolerance = abs(y[i] - point)
        
        if tolerance < tolerance_range:
            my_t = t[i]
            tolerance_range = tolerance
    
    return my_t

