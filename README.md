# Geocoding Proxy Service

## Setup
1. Copy `config.secret.json.example` to `config.secret.json`.
2. Save credentials for geocoding services.

   a. Google

      1. Navigate to https://developers.google.com/maps/documentation/geocoding/start.
      2. Click "Get a Key" in the upper-right and follow the instructions.
      3. Copy the provided API key.
      4. Save it into the `JSON` field `google.api_key_params.key` in `config.secret.json`.

   b. Here

      1. Sign up for an account at https://developer.here.com/authenticationpage.
      2. Navigate to https://developer.here.com/projects and create a project.
      3. On the project page, copy the provided app ID and app key.
      4. Save them into the `JSON` field `here.api_key_params.app_id` and
      `here.api_key_params.app_key`, respectively, in `config.secret.json`.

3. _OPTIONAL_ Add other geo services, following the templates for given services.

## Usage

### API
1. Run the server `./main.py serve`.
2. `POST` to `http://localhost:6305/` (6305 for "GEOS" :P) with a `JSON` body that contains
an address in the `"address"` field.

### CLI
1. `./main.py get_coords [address]`.