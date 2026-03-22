def calculate_risk(customer):
    tickets = customer["tickets_last_30_days"]
    charges_increase = customer["charges_increase"]
    contract = customer["contract"]
    complaint = customer["complaint_ticket"]

    if tickets > 5:
        return "HIGH"

    if charges_increase and tickets >= 3:
        return "MEDIUM"

    if contract == "Month-to-Month" and complaint:
        return "HIGH"

    return "LOW"