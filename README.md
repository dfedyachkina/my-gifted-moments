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

