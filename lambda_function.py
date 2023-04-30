from aws_lambda_powertools.utilities.feature_flags import AppConfigStore, FeatureFlags
app_config = AppConfigStore(environment="dev", application="mgt", name="features")

feature_flags = FeatureFlags(store=app_config)

def lambda_handler(event, context):
    maintenance_mode = feature_flags.evaluate(name="weekend_maintenance", default=False)
    if maintenance_mode:
        return {"status": 503, "body":"System down for maintenance"}
    else:
        # handle logic
        return {"status": 200, "body":"Success"}