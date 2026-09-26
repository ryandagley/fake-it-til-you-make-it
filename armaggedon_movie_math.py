from math import pi

R_EARTH_KM = 6371 # radius of earth in kms
V_SEP_MPS = 5.0  # generous sideways kick, speed of the parts

BEATS = {
    "discovery (18 days)": 18 * 24,   # 432 h, when they found out about it
    "touchdown / start drill": 12,    # NASA's 12 hour plan, plant bomb within 8h and explode NLT 4h to impact
    "zero barrier": 4,  # What NASA said we have to explode by to survive
    "Harry's click (~18 min)": 0.3,  # What actually happened
}

def hit_odds(hours_left: float, n_frag: int = 2) -> float:
    cloud_r = V_SEP_MPS * max(hours_left, 1e-6) * 3.6  # km
    p_one = min(1.0, (R_EARTH_KM / max(cloud_r, 1)) ** 2)
    return 1 - (1 - p_one) ** n_frag

for label, h in BEATS.items():
    print(f"{label:28} {h:>6.1f} h  →  {hit_odds(h):.0%} still hits")
