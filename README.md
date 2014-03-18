# Blog Coding Challenge
Make a Blog with distinct Categories and Authors. If time permits, add the ability to add Comments. Take about 30 minutes - get as far as you can and we'll discuss.

## Requirements
1. Framework should be Django or Flask.
2. Views:
    * List view (all posts)
    * Filtered list view by category
    * Detail view (single post)
    * Process comment submissions
3. CMS to create data

## Up To You
1. Backend: Use whatever you're comfortable with (models + sql/monogo/redis).
2. Models: Model the data in the way that seems the most fit to you.
3. Tests: If you have time; obviously doesn't have to be full coverage, we just want to get a sense of your approach to testing.

## Not Required
1. Templates: I don't need to see any template code.
2. Auth: Don't worry about authentication (assume any anonymous user can create comments and blog posts).
3. Since time is a factor, mock up whatever modules you don't have time to code.


----------

## What We're Looking At
1. Is the backend modeled in a sane way?
2. What framework did they use? Did they implement it correctly?
3. Did they leverage on existing libraries?
    * Did they use Django's admin?
    * Did they use class based views?
4. Is the urls file sane?
    * Did they use named urls?
5. Did they use ModelForms for submission of comments?

## Bonus
1. Virtualenv + pip
2. Tests
3. CRSF token validation
