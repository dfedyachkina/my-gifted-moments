# [my-gifted-moments](https://my-gifted-moments-154948e92f6b.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/dfedyachkina/my-gifted-moments)](https://www.github.com/dfedyachkina/my-gifted-moments/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/dfedyachkina/my-gifted-moments)](https://www.github.com/dfedyachkina/my-gifted-moments/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/dfedyachkina/my-gifted-moments)](https://www.github.com/dfedyachkina/my-gifted-moments)


![screenshot](documentation/mockup.png)

source: [my-gifted-moments amiresponsive](https://ui.dev/amiresponsive?url=https://my-gifted-moments-154948e92f6b.herokuapp.com)

> [!IMPORTANT]
> The examples in these templates are strongly influenced by the Code Institute walkthrough project called "Boutique Ado".

## UX

### The 5 Planes of UX

#### 1. Strategy Plane
##### Purpose
- Deliver a delightful, stress-free shopping experience tailored for gifting needs.
- Make it simple for customers to customize gifts and add personal touches (e.g., notes, messages).
- Enable store admins to efficiently manage product availability, seasonal items, and orders.

##### Primary User Needs
- Shoppers (guests or registered): Need to explore gift categories, customize bundles, and checkout smoothly.
- Site Admins: Need tools to manage seasonal items, promotions, stock levels, and manage orders.

##### Business Goals
- Boost Sales by Creating a Seamless and Delightful Gifting Experience.
- Foster Customer Loyalty Through Personalization and Smart Account Features.
- Ensure a Curated, Well-Maintained Gift Collection.

#### 2. Scope Plane
##### Features
- A full list of [Features](#features) can be viewed in detail below.

##### Content Requirements
- Gift details, including name, price, description, category, and images.
- Clear prompts and instructions for browsing, filtering, and purchasing.
- Order details, confirmation pages, and email notifications.
- Secure payment processing using Stripe.
- Payment success emails sent to users.
- Favorite list contains the gifts which user marked as Favorite.
- Profile contains default delivery information which may be modified by user and order history.
- FAQ page contains frequntely asked question and answers to them.
- Contact Us page contains the form which user might send directly to admin.
- Newsletter contains the form to activate a subscription for sending mails to him. 
- 404 page for lost users.

#### 3. Structure Plane
##### Information Architecture
- **Navigation Menu**:
  - Links to Home, Gifts, Cart, FAQ, Contact Us, Newsletter and Account sections.
- **Hierarchy**:
  - Prominent gift categories and filters for easy navigation.
  - Cart and checkout options displayed prominently for convenience.
  - Favorite List and Gift Management options displayed under account section

##### User Flow
1. Guest user browses the store → filters and sorts products by category, occasion, price, or name.
2. Guest user adds items to the cart → proceeds to checkout.
3. Guest user creates an account or logs in during checkout → completes purchase.
4. Guest user can browse FAQ page → see frequently asked questions and expand answers.
5. Guest user can browse Contact us page → can fill the form, submit it and receive suceess message.
6. Returning customers log in → view past orders and track purchase history.
7. Registred users add items to favorite list → view favorite list, add to favorite list and remove from favorite list.
8. Site owners manage inventory → add, update, or delete products and categories.
9. Site owners manage orders → add, change and see orders.
10. Site owners manage FAQs → can add a new question, edit and delete it.
11. Site owners manage Contact Us submited forms → receive a mail who jas submitted the form and filled infromation.
12. Site owners browse subscription → browse, add and delete users who has subsribed to newsletter.
13. Users signup to the newsletter → potentially receive advanced notice of upcoming sales.
14. User get error 404 → when user goes to the path which doesn't exist - he gets the 404 error.

#### 4. Skeleton Plane
##### Wireframe Suggestions
- A full list of [Wireframes](#wireframes) can be viewed in detail below.

#### 5. Surface Plane
##### Visual Design Elements
- **[Colours](#colour-scheme)**: see below.
- **[Typography](#typography)**: see below.

### Colour Scheme

I used [coolors.co](https://coolors.co/080708-3772ff-df2935-fdca40-e6e8e6) to generate my color palette.

- `#333` primary text.
- `#ffffff` primary highlights.
- `#555` secondary text.
- `#555` secondary highlights.

![screenshot](documentation/coolors.png)

### Typography


- [Playfair Display](https://fonts.google.com/specimen/PlayfairDisplay) was used for the primary headers and titles.
- [Lato](https://fonts.google.com/specimen/Lato) was used for all other secondary text.
- [Imperial Script](https://fonts.google.com/specimen/ImperialScript) was used for word Moment on home banner.
- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer.

## User Stories

| Target | Expectation | Outcome |
| --- | --- | --- |
| As a guest user | I would like to browse gifts without needing to register | so that I can shop freely before deciding to create an account. |
| As a guest user | I would like to be prompted to create an account or log in at checkout | so that I can complete my purchase and track my order history. |
| As a guest user | I would like to browse FAQ page | so that I can find an answer to my question and get know more about store. |
| As a guest user | I would like to browse Contact Us page | so that I can fill the form and submit in case if I have a question or I want to be contacted by the store employee regarding my query. |
| As a user | I would like to sign up to the site's newsletter | so that I can stay up to date with any upcoming sales or promotions. |
| As a customer | I would like to browse various gift categories | so that I can easily find what I'm looking for. |
| As a customer | I would like to sort gifts by price (low-to-high/high-to-low) and name (alphabetical) | so that I can quickly organize items in a way that suits my shopping style. |
| As a customer | I would like to filter gifts by category | so that I can narrow down the gifts to the types I am most interested in. |
| As a customer | I would like to filter gifts by occasion | so that I can narrow down the gifts to the occasions I am most interested in. |
| As a customer | I would like to click on individual gifts to view more details (description, price, image, etc.) | so that I can make an informed decision about my purchase. |
| As a customer | I would like to add items to favorite list | so that I can make back to them if I would like to purchase them later. |
| As a customer | I would like to add items to my shopping cart using quantity increment/decrement buttons | so that I can adjust how many units of a product I want before checkout. |
| As a customer | I would like to view and manage my shopping cart | so that I can review, add, or remove items before proceeding to checkout. |
| As a customer | I would like to adjust the quantity of items in my cart | so that I can modify my purchase preferences without leaving the cart. |
| As a customer | I would like to remove items from my cart | so that I can remove gifts I no longer wish to buy. |
| As a customer | I would like to proceed to checkout where I see my cart items, grand total, and input my name, email, shipping address, and card details | so that I can complete my purchase. |
| As a customer | I would like to receive a confirmation email after my purchase | so that I can have a record of my transaction and order details. |
| As a customer | I would like to see an order confirmation page with a checkout order number after completing my purchase | so that I know my order has been successfully placed. |
| As a customer | I would like to securely enter my card details using Stripe at checkout | so that I can feel confident my payment information is protected. |
| As a returning customer | I would like to be able to log in and view my past orders | so that I can track my previous purchases and order history. |
| As a returning customer | I would like the checkout process to remember my shipping address | so that future purchases are quicker and easier. |
| As a site owner | I would like to create new products with a name, description, price, images, and category | so that I can add additional items to the store inventory. |
| As a site owner | I would like to update product details (name, price, description, image, category) at any time | so that I can keep my product listings accurate and up to date. |
| As a site owner | I would like to delete products that are no longer available or relevant | so that I can maintain a clean and accurate inventory. |
| As a site owner | I would like to view all orders placed on the website | so that I can track and manage customer purchases. |
| As a site owner | I would like to manage product categories | so that I can ensure items are correctly organized and easy for customers to find. |
| As a site owner | I would like to manage product occasions | so that I can add more ocassions at the time of celebration of big events such as Christmas, Easter etc. |
| As a site owner | I would like to manage frequently asked questions| so that I can keep questions are updated and add new questions which customers ask often
| As a site owner | I would like to manage contact forms and receive them on my email | so that I can see which person want to be contacted and what's his question, it would decrease waiting time and allow me to reply as soon as possible  |
| As a user | I would like to see a 404 error page if I get lost | so that it's obvious that I've stumbled upon a page that doesn't exist. |

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

| Page | Mobile | Tablet | Desktop |
| --- | --- | --- | --- |
| Register | ![screenshot](documentation/wireframes/mobile-register.png) | ![screenshot](documentation/wireframes/tablet-register.png) | ![screenshot](documentation/wireframes/desktop-register.png) |
| Login | ![screenshot](documentation/wireframes/mobile-login.png) | ![screenshot](documentation/wireframes/tablet-login.png) | ![screenshot](documentation/wireframes/desktop-login.png) |
| Logout | ![screenshot](documentation/wireframes/mobile-logout.png) | ![screenshot](documentation/wireframes/tablet-logout.png) | ![screenshot](documentation/wireframes/desktop-logout.png) |
| Profile | ![screenshot](documentation/wireframes/mobile-profile.png) | ![screenshot](documentation/wireframes/tablet-profile.png) | ![screenshot](documentation/wireframes/desktop-profile.png) |
| Home | ![screenshot](documentation/wireframes/mobile-home.png) | ![screenshot](documentation/wireframes/tablet-home.png) | ![screenshot](documentation/wireframes/desktop-home.png) |
| Gifts | ![screenshot](documentation/wireframes/mobile-gifts.png) | ![screenshot](documentation/wireframes/tablet-gifts.png) | ![screenshot](documentation/wireframes/desktop-gifts.png) |
| Gift Details | ![screenshot](documentation/wireframes/mobile-gift-details.png) | ![screenshot](documentation/wireframes/tablet-gift-details.png) | ![screenshot](documentation/wireframes/desktop-gift-details.png) |
| Bag | ![screenshot](documentation/wireframes/mobile-bag.png) | ![screenshot](documentation/wireframes/tablet-bag.png) | ![screenshot](documentation/wireframes/desktop-bag.png) |
| Checkout | ![screenshot](documentation/wireframes/mobile-checkout.png) | ![screenshot](documentation/wireframes/tablet-checkout.png) | ![screenshot](documentation/wireframes/desktop-checkout.png) |
| Checkout Success | ![screenshot](documentation/wireframes/mobile-checkout-success.png) | ![screenshot](documentation/wireframes/tablet-checkout-success.png) | ![screenshot](documentation/wireframes/desktop-checkout-success.png) |
| My favorite list | ![screenshot](documentation/wireframes/mobile-my-favorite-list.png) | ![screenshot](documentation/wireframes/tablet-my-favorite-list.png) | ![screenshot](documentation/wireframes/desktop-my-favorite-list.png) |
| Add Gift | ![screenshot](documentation/wireframes/mobile-add-gift.png) | ![screenshot](documentation/wireframes/tablet-add-gift.png) | ![screenshot](documentation/wireframes/desktop-add-gift.png) |
| Edit Gift| ![screenshot](documentation/wireframes/mobile-edit-gift.png) | ![screenshot](documentation/wireframes/tablet-edit-gift.png) | ![screenshot](documentation/wireframes/desktop-edit-gift.png) |
| Newsletter | ![screenshot](documentation/wireframes/mobile-newsletter.png) | ![screenshot](documentation/wireframes/tablet-newsletter.png) | ![screenshot](documentation/wireframes/desktop-newsletter.png) |
| Contact | ![screenshot](documentation/wireframes/mobile-contact.png) | ![screenshot](documentation/wireframes/tablet-contact.png) | ![screenshot](documentation/wireframes/desktop-contact.png) |
| FAQ | ![screenshot](documentation/wireframes/mobile-faq.png) | ![screenshot](documentation/wireframes/tablet-faq.png) | ![screenshot](documentation/wireframes/desktop-fag.png) |
| 404 | ![screenshot](documentation/wireframes/mobile-404.png) | ![screenshot](documentation/wireframes/tablet-404.png) | ![screenshot](documentation/wireframes/desktop-404.png) |

## Features

### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Register | Authentication is handled by allauth, allowing users to register accounts. | ![screenshot](documentation/features/register.png) |
| Login | Authentication is handled by allauth, allowing users to log in to their existing accounts. | ![screenshot](documentation/features/login.png) |
| Logout | Authentication is handled by allauth, allowing users to log out of their accounts. | ![screenshot](documentation/features/logout.png) |
| Home | Home page shows a banner and link to shop. | ![screenshot](documentation/features/home.png) |
| Gift List | Users can browse all available products with sorting, filtering by categories, and search functionality. | ![screenshot](documentation/features/gifts.png) |
| Gift Details | Displays detailed information about a selected product, including its name, description, price, an image, and available sizes. | ![screenshot](documentation/features/gift-details.png) |
| Add to Bag | Users can add items to their shopping bag, with support for selecting different sizes if applicable. | ![screenshot](documentation/features/add-to-bag.png) |
| View Bag | Users can view the contents of their shopping bag, adjust quantities, or remove items. | ![screenshot](documentation/features/bag.png) |
| Checkout | Users can proceed to checkout, where they provide their delivery details and payment information using Stripe integration. | ![screenshot](documentation/features/checkout.png) |
| Order Confirmation | Users receive an on-screen and email confirmation with details of their purchase. | ![screenshot](documentation/features/checkout-success.png) |
| Profile Management | Users can manage their profile information, including their default delivery address and order history. | ![screenshot](documentation/features/profile.png) |
| Order History | Users can view their past orders and access details of each order, including products purchased and the delivery status. | ![screenshot](documentation/features/order-history.png) |
| Add to favorite list | Users can add liked items to favorite list. | ![screenshot](documentation/features/add-to-favorite-list.png) |
| Favorite List | Users can browse items which he added to favorite list. | ![screenshot](documentation/features/favorite-list.png) |
| Gift Management | Superusers can add, edit, and delete products from the site via a CRUD interface. | ![screenshot](documentation/features/gift-management.png) |
| Newsletter | Users can register their email address to receive newsletters from the site. Currently, this only stores the email in the database. | ![screenshot](documentation/features/newsletter.png) |
| Contact | Users can submit a message via the contact form, which stores their name, email, and message in the database. | ![screenshot](documentation/features/contact.png) |
| FAQs | Admins can manage frequently asked questions, which are displayed on the site for users. | ![screenshot](documentation/features/faq.png) |
| Heroku Deployment | The site is deployed to Heroku, making it accessible online for users. | ![screenshot](documentation/features/heroku.png) |
| SEO | SEO optimization with a sitemap.xml, robots.txt, and appropriate meta tags to improve search engine visibility. | ![screenshot](documentation/features/seo.png) |
| Marketing | Social media presence is available in the footer using external links, as well as a Facebook Marketplace wireframe in the README for future integrations. | ![screenshot](documentation/features/marketing.png) |
| 404 | The 404 error page will indicate when a user has navigated to a page that doesn't exist, replacing the default Heroku 404 page with one that ties into the site's look and feel. | ![screenshot](documentation/features/404.png) |

### Future Features

- **Gift Reviews & Ratings**: Allow customers to leave reviews and rate products, with admin moderation. Display average ratings and review counts on product pages.
- **Discount Codes and Vouchers**: Allow the admin to create discount codes or vouchers for promotions and marketing campaigns.
- **Loyalty Program**: Introduce a points-based loyalty system where customers earn points for purchases, which can be redeemed for discounts.
- **Multi-Currency and Multi-Language Support**: Expand the application to support multiple currencies and languages to reach a global audience.
- **Product Bundles**: Offer discounted product bundles (e.g., buy 3 for the price of 2) or custom product kits.
- **Social Media Integration**: Enable users to share products directly to social media platforms or implement a social login for quick account creation.
- **Shipping Tracking Integration**: Provide real-time shipping updates and tracking information directly within the user’s order history.
- **Advanced Analytics Dashboard for Admin**: Offer an in-depth dashboard that displays sales trends, popular gifts, customer behavior, and more.
- **Mobile App**: Develop a mobile app for iOS and Android, providing users with a more optimized shopping experience on mobile devices.

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) | Cloud-based IDE for development. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/jQuery-grey?logo=jquery&logoColor=0769AD)](https://jquery.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/Stripe-grey?logo=stripe&logoColor=008CDD)](https://stripe.com) | Online secure payments of e-commerce products/services. |
| [![badge](https://img.shields.io/badge/Gmail_API-grey?logo=gmail&logoColor=EA4335)](https://mail.google.com) | Sending emails in my application. |
| [![badge](https://img.shields.io/badge/Canva-grey?logo=canva&logoColor=00C4CC)](https://www.canva.com/p/canvawireframes) | Creating favicon and logo |
| [![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) | Icons. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/Mermaid-grey?logo=mermaid&logoColor=FF3670)](https://mermaid.live) | Generate an interactive diagram for the data/schema. |


## Database Design

### Data Model

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models. Understanding the relationships between different tables can save time later in the project.

![screenshot](documentation/erd.png)

I have used `Mermaid` to generate an interactive ERD of my project.

```mermaid
erDiagram
    User {
        int id PK
        varchar username
        varchar email
        varchar password
    }

    UserProfile {
        int id PK
        varchar default_phone_number
        varchar default_street_address1
        varchar default_street_address2
        varchar default_town_or_city
        varchar default_county
        varchar default_postcode
        varchar default_country
        int user_id FK
    }

    User ||--|| UserProfile : has_one

    Occasion {
        int id PK
        varchar name
    }

    Category {
        int id PK
        varchar name
        varchar friendly_name
    }

    Gift {
        int id PK
        varchar name
        text description
        bool has_sizes
        decimal price
        varchar image_url
        image image
        int category_id FK
        int occasion_id FK
    }

    Gift ||--o| Category : belongs_to
    Gift ||--o| Occasion : for

    "Order" {
        int id PK
        varchar order_number
        varchar full_name
        varchar email
        varchar phone_number
        varchar country
        varchar postcode
        varchar town_or_city
        varchar street_address1
        varchar street_address2
        varchar county
        datetime date
        decimal delivery_cost
        decimal order_total
        decimal grand_total
        text original_bag
        varchar stripe_pid
        int user_profile_id FK
    }

    OrderLineItem {
        int id PK
        int quantity
        decimal lineitem_total
        varchar product_size
        int gift_id FK
        int order_id FK
    }

    "Order" ||--o| OrderLineItem : has_many
    OrderLineItem ||--o| Gift : contains
    "Order" ||--o| UserProfile : belongs_to

    Favorite {
        int id PK
        int user_id FK
        int gift_id FK
        datetime added_at
    }

    User ||--o| Favorite : has_many
    Gift ||--o| Favorite : is_favorited

    Newsletter {
        int id PK
        varchar email
    }

    Contact {
        int id PK
        varchar name
        varchar email
        text message
    }

    FAQ {
        int id PK
        varchar question
        text answer
    }

```

source: [Mermaid](https://mermaid.live/edit#pako:eNqVVcFu2zAM_RVD57RIHLdpfRs6DBg2bB2GXYYAhmIxjlBZcimqqdvk3yfbSVPHceP5kBh8TyRFPtKvLDUCWMwAP0ueIc_nOvDPHwsYvDbv1SM1BVIE998OpieO6Ypj4DxV8xy6CORcqq654NauDYoG2c71IeQ9mqVUMDCygCV3ipJiZTQk2uULwH6WJQSghAuBYO1kKDHsJ5JZ68Rgkkoq-1mpcfojvDCWqiac8YDliXoFm83FxWbTql0crLhNfEX2xDtOkBksB1b1dC-XKEELVSYH-C0TH1m4lAb6tw_uXFCCZ_K3tynKgqTRB2RhjKrvZ-UL2INdQCpzroICZQpdM3KSOuuG9WAGicN3Kq1NzW_PNauam82hrHGwAGV0Zr0g9tyfKAYPkKm4vfJdOqWS_5uvD8ehJabWsV4dfqzzs3N1dp6OJ0T4ypLMoX7pNlOAkk-ApZ8LS124KScZ4qoL-g2nxTFYy82gzKTmKlnw7OQdZAFJIY-3Vt3o71LDV4L8TMMr06Pjmlp13KemvBPpnRxn99afRn618k8lsddlO6NmG-Rcl6fy3R3ZK7tfyTtie890yT9gbRUQDdb-Owm_3ebOaOKD18mg0ag7nHv1daf6y6dfAyM9OrDtbVS75dqu94O2ZSOWA_rgwn9Ta7dzRivwKbLYvwqOD3M21xWPOzK_S52ymNDBiLmikvvuK8ziJVfWWwuuWfzKnlk8jSaXN9ez8HoyHc_C8TiajVjJ4ovp5XUUTqMovLqdXd2Et-FsO2Ivxngfk8vxZBpGkT_m_zxW-_tbY01QNC5b7YJt_wE0ZoQj)


I have used `pygraphviz` and `django-extensions` to auto-generate an ERD.

The steps taken were as follows:
- In the terminal: `sudo apt update`
- then: `sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config`
- then type `Y` to proceed
- then: `pip3 install django-extensions pygraphviz`
- in my `settings.py` file, I added the following to my `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'django_extensions',
    ...
]
```
- back in the terminal: `python3 manage.py graph_models -a -o erd.png`
- drag the new `erd.png` file into my `documentation/` folder
- removed `'django_extensions',` from my `INSTALLED_APPS`
- finally, in the terminal: `pip3 uninstall django-extensions pygraphviz -y`

![screenshot](documentation/advanced-erd.png)

source: [medium.com](https://medium.com/@yathomasi1/1-using-django-extensions-to-visualize-the-database-diagram-in-django-application-c5fa7e710e16)

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://www.github.com/dfedyachkina/my-gifted-moments/projects) served as an Agile tool for this project. Through it, EPICs, User Stories, issues/bugs, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![screenshot](documentation/gh-projects.png)

### GitHub Issues

[GitHub Issues](https://www.github.com/dfedyachkina/my-gifted-moments/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks, and tracked any issues/bugs.

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues/dfedyachkina/my-gifted-moments)](https://www.github.com/dfedyachkina/my-gifted-moments/issues) | ![screenshot](documentation/gh-issues-open.png) |
| [![GitHub closed issues](https://img.shields.io/github/issues-closed/dfedyachkina/my-gifted-moments)](https://www.github.com/dfedyachkina/my-gifted-moments/issues?q=is%3Aissue+is%3Aclosed) | ![screenshot](documentation/gh-issues-closed.png) |

### MoSCoW Prioritization

I've decomposed my Epics into User Stories for prioritizing and implementing them. Using this approach, I was able to apply "MoSCoW" prioritization and labels to my User Stories within the Issues tab.

- **Must Have**: guaranteed to be delivered - required to Pass the project (*max ~60% of stories*)
- **Should Have**: adds significant value, but not vital (*~20% of stories*)
- **Could Have**: has small impact if left out (*the rest ~20% of stories*)
- **Won't Have**: not a priority for this iteration - future features

## Ecommerce Business Model

Gifted Moments operates on a **Business to Customer (B2C) model**, catering directly to individual customers seeking thoughtful and unique gifts. It follows a straightforward B2C approach—focused on one-time purchases rather than subscriptions—making it easy for customers to find and buy the perfect gift without any long-term commitments.

Although still in the early stages of development, Gifted Moments already features a growing newsletter list and active links to its social media channels, laying the foundation for strong customer engagement.

Social media plays a key role in building a supportive and enthusiastic community around the brand. Platforms like Facebook and Instagram can help increase visibility, connect with loyal customers, and attract new visitors to the site through engaging content and promotions.

The newsletter allows Gifted Moments to stay in touch with its audience by sharing updates on new arrivals, exclusive offers, seasonal specials, store announcements, and upcoming events—keeping customers informed and connected.

## SEO & Marketing

### Keywords

I've identified some appropriate keywords to align with my site, that should help users when searching online to find my page easily from a search engine. This included a series of the following keyword types:

- Short-tail (head terms) keywords
- Long-tail keywords

I've also played around with [Word Tracker](https://www.wordtracker.com) a bit to check the frequency of some of my site's primary keywords (only until the free trial expired).

### Sitemap

I've used [XML-Sitemaps](https://www.xml-sitemaps.com) to generate a sitemap.xml file. This was generated using my deployed site URL: https://my-gifted-moments-154948e92f6b.herokuapp.com

After it finished crawling the entire site, it created a [sitemap.xml](sitemap.xml), which I've downloaded and included in the repository.

### Robots

I've created the [robots.txt](robots.txt) file at the root-level. Inside, I've included the default settings:

```txt
User-agent: *
Disallow:
Sitemap: https://my-gifted-moments-154948e92f6b.herokuapp.com/sitemap.xml
```

Further links for future implementation:
- [Google search console](https://search.google.com/search-console)
- [Creating and submitting a sitemap](https://developers.google.com/search/docs/advanced/sitemaps/build-sitemap)
- [Managing your sitemaps and using sitemaps reports](https://support.google.com/webmasters/answer/7451001)
- [Testing the robots.txt file](https://support.google.com/webmasters/answer/6062598)

### Social Media Marketing

Creating a strong social base (with participation) and linking that to the business site can help drive sales. Using more popular providers with a wider user base, such as Facebook, typically maximizes site views.

I've created a mockup Facebook business account using the [Balsamiq template](https://code-institute-org.github.io/5P-Assessments-Handbook/files/Facebook_Mockups.zip) provided by Code Institute.

![screenshot](documentation/mockup-facebook.png)

### Newsletter Marketing

I have incorporated a newsletter sign-up form on my application, to allow users to supply their email address if they are interested in learning more. 


**Custom Django Model Newsletter**

- Create a custom `newsletter` app in your project, with a custom model/class called `Newsletter`.
- This method satisfies two assessment criteria:
    1. include a newsletter
    2. one of your 3 required custom models
- It doesn't need anything except the `email` field on the model, but feel free to add more if you need.
- Example: (keep this in your README if you've done this method, attach your `Newsletter` model in a code block like the following example)
    ```python
    class Newsletter(models.Model):
        email = models.EmailField(null=False, blank=False)

        def __str__(self):
            return self.email
    ```
- Consider using the same `send_mail()` functionality used on the `webhook_handler.py` file.
    - You can trigger an email to be sent out to subscribed users when new products are added to the site!


## Testing

> [!NOTE]
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://my-gifted-moments-154948e92f6b.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py` file.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

| Key | Value |
| --- | --- |
| `ADMINS` | user-inserts-admins |
| `DATABASE_URL` | user-inserts-own-postgres-database-url |
| `DEBUG` | False |
| `DEFAULT_FROM_EMAIL` | user-inserts-store-email|
| `EMAIL_HOST_PASS` | user-inserts-own-gmail-api-key |
| `EMAIL_HOST_USER` | user-inserts-own-gmail-email-address |
| `SECRET_KEY` | any-random-secret-key |
| `STRIPE_PUBLIC_KEY` | user-inserts-own-stripe-public-key |
| `STRIPE_SECRET_KEY` | user-inserts-own-stripe-secret-key |

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.
- *Optional*: edit your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
    - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

> [!CAUTION]
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
    - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
	- `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
	- `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
	- `https://my-gifted-moments-154948e92f6b.herokuapp.com/checkout/wh/`
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here:
	- `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with **wh**)

### Gmail API

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for purchase order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

- Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Google Account settings**.
- From this new page, select **Security** on the left.
- Select **2-Step Verification** to turn it on. (*verify your password and account*)
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords** (*search for it at the top, if not*).
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
    - Any custom name, such as "Django" or `my-gifted-moments`
- You'll be provided with a 16-character password (API key).
    - Save this somewhere locally, as you cannot access this key again later!
    - If your 16-character password contains *spaces*, make sure to remove them entirely.
    - `EMAIL_HOST_PASS` = user's 16-character API key
    - `EMAIL_HOST_USER` = user's own personal Gmail email address

### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live Heroku site.

To include WhiteNoise in your own projects:

- Install the latest WhiteNoise package:
    - `pip install whitenoise`
- Update the `requirements.txt` file with the newly installed package:
    - `pip freeze --local > requirements.txt`
- Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE` list, above all other middleware (apart from Django’s "SecurityMiddleware"):

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # any additional middleware
]
```


### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.


Sample `env.py` file:

```python
import os

os.environ.setdefault("AWS_ACCESS_KEY_ID", "user-inserts-own-aws-access-key-id")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "user-inserts-own-aws-secret-access-key")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("EMAIL_HOST_PASS", "user-inserts-own-gmail-host-api-key")
os.environ.setdefault("EMAIL_HOST_USER", "user-inserts-own-gmail-email-address")
os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "user-inserts-own-stripe-public-key")
os.environ.setdefault("STRIPE_SECRET_KEY", "user-inserts-own-stripe-secret-key")
os.environ.setdefault("STRIPE_WH_SECRET", "user-inserts-own-stripe-webhook-secret")  # only if using Stripe Webhooks

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("DEVELOPMENT", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (*Windows/Linux*) or `⌘+C` (*Mac*)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (*if applicable*): `python3 manage.py loaddata file-name.json` (*repeat for each file*)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*
- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/dfedyachkina/my-gifted-moments).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/dfedyachkina/my-gifted-moments.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://www.github.com/dfedyachkina/my-gifted-moments)

**Please Note**: in order to directly open the project in Gitpod, you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/dfedyachkina/my-gifted-moments).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits


### Content

| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [Boutique Ado](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Bootstrap](https://getbootstrap.com) | Various components / responsive front-end framework |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [Stripe](https://docs.stripe.com/payments/elements) | Online payment services |
| [Gmail API](https://developers.google.com/gmail/api/guides) | Sending payment confirmation emails |
| [ChatGPT](https://chatgpt.com) | Help with code logic and explanations |

### Media

| Source | Notes |
| --- | --- |
| [favicon.io](https://favicon.io) | Generating the favicon |
| [Font Awesome](https://fontawesome.com) | Icons used throughout the site |
| [Pexels](https://images.pexels.com/photos/416160/pexels-photo-416160.jpeg) | Hero image |
| [Wallhere](https://c.wallhere.com/images/9c/c8/da4b4009f070c8e1dfee43d25f99-2318808.jpg!d) | Background wallpaper |
| [Pixabay](https://cdn.pixabay.com/photo/2017/09/04/16/58/passport-2714675_1280.jpg) | Background wallpaper |
| [DALL-E 3](https://openai.com/index/dall-e-3) | AI generated artwork |
| [CompressPNG](https://compresspng.com) | Compressing images > 5MB |
| [CloudConvert](https://cloudconvert.com/webp-converter) | Converting images to `.webp` |

### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for the support throughout the development of this project.
