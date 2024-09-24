from msgraph import GraphServiceClient
from azure.identity.aio import ClientSecretCredential
import configparser

env_file = configparser.ConfigParser()
env_file.read('.env')

credential = ClientSecretCredential(
       tenant_id=env_file["API KEYS"]["TENANT_ID"],
       client_id=env_file["API KEYS"]["CLIENT_ID"],
       client_secret=env_file["API KEYS"]["CLIENT_SECRET"],
   )


graph_client = GraphServiceClient(credentials=credential)

async def get_number_of_available_licenses():
    result = await graph_client.subscribed_skus.by_subscribed_sku_id('2091c68c-b55a-4e92-8cc9-90c2085ca9c0_cbdc14ab-d96c-4c30-b9f4-6ada7cdc1d46').get()

    return result.prepaid_units.enabled - result.consumed_units

# test = asyncio.run(get_number_of_available_licenses())