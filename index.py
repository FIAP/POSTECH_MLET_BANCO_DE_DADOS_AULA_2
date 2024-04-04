import boto3

# Step 1: Configure Boto3 to use LocalStack
dynamodb = boto3.resource('dynamodb',
                          endpoint_url='http://localhost:9000',  # Default LocalStack DynamoDB endpoint
                          region_name='us-west-2',  # Example region, can be any
                          aws_access_key_id='test',  # Dummy AWS access key for LocalStack
                          aws_secret_access_key='test')  # Dummy AWS secret key for LocalStack

# Step 2: Create a DynamoDB table
def create_table():
    table = dynamodb.create_table(
        TableName='fiap',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'  # Partition key
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    # Wait for the table to be created
    table.wait_until_exists()
    print("Table created successfully.")

# Step 3: Insert an item into the table
def create_item():
    table = dynamodb.Table('fiap')
    table.put_item(
       Item={
            'id': '001',
            'name': 'Thiago S Adriano',
            'age': 38
        }
    )
    print("Item created successfully.")

# Step 4: Read an item from the table
def read_item():
    table = dynamodb.Table('fiap')
    response = table.get_item(
        Key={
            'id': '001'
        }
    )
    item = response.get('Item', {})
    print(f"Read item: {item}")

# Step 5: Update an item in the table
def update_item():
    table = dynamodb.Table('fiap')
    table.update_item(
        Key={
            'id': '001'
        },
        UpdateExpression='SET age = :val1',
        ExpressionAttributeValues={
            ':val1': 39
        }
    )
    print("Item updated successfully.")

# Step 6: Delete an item from the table
# def delete_item():
#     table = dynamodb.Table('fiap')
#     table.delete_item(
#         Key={
#             'id': '001'
#         }
#     )
#     print("Item deleted successfully.")

if __name__ == "__main__":
    # Create DynamoDB table
    #create_table()
        
    # Perform CRUD operations
    create_item()
    read_item()
    update_item()
    read_item()
    #delete_item()
