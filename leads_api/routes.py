def includeme(config):
    # Buyers
    config.add_route(
        'v1_buyers_tiers_makes_coverage',
        '/v1/buyers_tiers/{buyer_tier_slug}/makes/{make_slug}/coverage',
    )

    # Lead Quality (aka Scrub)
    config.add_route('v1_lead_quality_request', '/v1/lead_quality/{service}/')
    config.add_route('v1_lead_quality_status', '/v1/lead_quality/{service}/{id}')
