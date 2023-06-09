---
{"dg-publish":true,"permalink":"/building-a-cloud-environment/","title":"Building a Cloud Environment","tags":["cloudcomputing"],"created":"2023-05-04","updated":""}
---


# Building a Cloud Environment / Cloud Infrastructure 

Choose the **cloud infrastructure** based on your business use case 
Types of cloud infrastructure - 
## Private
completely dedicated to one end user or group, maintained on a private network
two types: 
### 1. Dedicated cloud infrastructure 
IT infrastructure is devoted to a single client with totally segregated access
### 2. Managed private cloud
 third-party provider deploys, configures, and manages a private cloud on behalf of its customers
## Public 
third party cloud providers who provide services over the Internet; eg Microsoft Azure, AWS 
## Hybrid 
combination of private and public 
combines on-premises infrastructure—or a private cloud—with a public cloud 
edge computing 
## Multi-cloud 
A multi-cloud architecture consists of multiple cloud services from various public or private cloud vendors. **All hybrid cloud environments are multi-clouds**. However, not all multi-cloud environments are hybrid clouds.


<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/cloud-delivery-models/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">





(aka cloud service delivery model)

# at a glance
**specific, pre-packaged combination of IT resources offered by a cloud provider**

**in terms of customizability and level of control/access granted, IaaS > PaaS > SaaS** 
mnemonic - <mark>I P S</mark>

in terms of ready-to-use, SaaS > PaaS > IaaS

# cloud service delivery models 

## IaaS - Infrastructure as a service
> Resources, self-contained IT environment 
> hardware, network, connectivity are all provided by cloud provider 
> bare infrastructure
> "bare metal"

generally offered as virtual instances

access = full access to virtualized infrastructure related IT resources

cloud consumer - sets up and configures bare infrastructure, manages, monitors software 

cloud provider - provides and manages IT resources like storage, processing, hosting, networking. monitors usage 

**offers as much configurability and customizability as on-premise tech**
**virtual servers**

eg. ec2

## PaaS - Platform as a service
>**ready made environment**
>support the entire device lifecycle
>provides a framework

allows customers to build, test, deploy run, update and scale applications more quickly and cost-effectively than they could if they had to build out and manage their own on-premises platform

access - moderate level of administrative control
limited administrative

cloud consumer - develops, tests, deploys, and manages

cloud provider - pre-configures infrastructure, middleware. monitors usage

eg Heroku 

## SaaS - Software as a service 
software that is  a shared cloud service
used to make a reusable cloud service widely available 
**mostly for end users**

access = front-end user-interface

cloud consumer - uses and configures cloud service

cloud provider - implements and manages cloud service 

eg. Gmail, Microsoft 365,

# Pizza analogy 
- **on-premise** -> your own kitchen, your own ingredients, any type of pizza
- **IaaS** -> (**kitchen** as a service) -> cloud provider manages kitchen, your own ingredients, any type of pizza
- **PaaS** -> (**take and bake**) -> cloud provider manages kitchen and some ingredients, your own pizza but with limited ingredients 
- **SaaS** -> (**pizza delivery**) -> cloud provider manages kitchen, ingredients, and pizza making. You can choose from available options 

**Ease of use vs Customizability**


>[!QUESTION]- Doubts
>netlify - saas, paas?
>cdn





</div></div>
