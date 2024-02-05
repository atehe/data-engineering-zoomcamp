if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test





@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    # Remove rows where the passenger count is equal to 0 or the trip distance is equal to zero.\
    data = data[data.trip_distance > 0]
    data = data[data.passenger_count > 0]

    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    print(data.VendorID.unique())

    data.rename(columns={'VendorID':'vendor_id', 'RatecodeID': 'ratecode_id',"PULocationID": 'pu_location_id', 
"DOLocationID": 'du_location_id'}, inplace=True)

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert (output.trip_distance > 0).sum() > 0, 'No data with trip distance > 0'
    assert (output.passenger_count > 0).sum() > 0, 'No data with passenger count > 0' 
    assert 'vendor_id' in output.columns, 'vendor_id not in data columns'


