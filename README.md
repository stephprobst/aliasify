# aliasify

## Supported environemnts:

This project is in an early state and has only been tested on Windows 10 with Python 3.9 and Python 3.10.

## Installation:

Install aliasify using pip:

```cmd
pip install aliasify
```

The required language model for entity detection (~500mb) will automatically be downloaded the first time you run the program.

## Remove language model again
The language model is installed as an independent python package. To free up space and remove it again use the following command:

```cmd
pip uninstall en_core_web_trf
```

## Usage:

Start the program using the command line:

```cmd
aliasify
```

Alternativelly (e.g. in an environment with blocked executables) start the program from a python session:

```python
import aliasify
aliasify.run()
```

Once the program has started, you can use the following workflow:

- Copy a text into your clipboard.
- Press F9 to replace all entities in the text with placeholders.
- Use the text in chatGPT, e.g. ask ChatGPT to shorten it.
- Copy the response into your clipboard.
- Press F10 to restore the orginal entities in the modified text.

## Example:

Copy the following text:

```txt
Subject: Invitation to attend the International Conference on Climate Change

Dear Dr. James Smith,

I hope this email finds you well. My name is Maria Perez, and I am writing to invite you to the International Conference on Climate Change, which will be held in Geneva, Switzerland from May 1-4, 2023.

We have reviewed your research on climate change and the impact of carbon emissions on the environment, and believe that your insights and expertise would make a valuable contribution to our conference. We are particularly interested in your recent paper on the effects of climate change on marine ecosystems, which was published in the Journal of Environmental Science last year.

The conference will bring together leading experts, scientists, and policymakers from around the world to discuss the latest research and innovations in the field of climate change. This year's theme is "Innovative Solutions for a Sustainable Future", and we believe that your research aligns well with this focus.

In addition to presenting your research, you will have the opportunity to network with other experts in your field, attend panel discussions, and participate in workshops. The conference will also feature a keynote address from Dr. Rajesh Sharma, the director of the Climate Change Division at the United Nations.

We would be delighted if you could join us in Geneva for this important event. Please let us know if you are able to attend, and we will provide you with further details and instructions for registration.

Thank you for your consideration, and we look forward to hearing from you soon.

Best regards,

Maria Perez

Conference Coordinator

International Conference on Climate Change

Geneva, Switzerland
```

Now, with the running aliasify program, press F9 and paste the text into chatGPT:

```txt
Subject: Invitation to attend <<EVENT_000018>>

Dear Dr. <<PERSON_000019>>,

I hope this email finds you well. My name is <<PERSON_000020>>, and I am writing to invite you to <<EVENT_000018>>, which will be held in <<GPE_000022>>, <<GPE_000023>> from <<DATE_000024>>.

We have reviewed your research on climate change and the impact of carbon emissions on the environment, and believe that your insights and expertise would make a valuable contribution to our conference. We are particularly interested in your recent paper on the effects of climate change on marine ecosystems, which was published in <<ORG_000025>> <<DATE_000026>>.

The conference will bring together leading experts, scientists, and policymakers from around the world to discuss the latest research and innovations in the field of climate change. This <<DATE_000027>>'s theme is "Innovative Solutions for a Sustainable Future", and we believe that your research aligns well with this focus.

In addition to presenting your research, you will have the opportunity to network with other experts in your field, attend panel discussions, and participate in workshops. The conference will also feature a keynote address from Dr. <<PERSON_000028>>, the director of <<ORG_000029>> at <<ORG_000030>>.

We would be delighted if you could join us in <<GPE_000022>> for this important event. Please let us know if you are able to attend, and we will provide you with further details and instructions for registration.

Thank you for your consideration, and we look forward to hearing from you soon.

Best regards,

<<PERSON_000020>>

Conference Coordinator

<<EVENT_000035>>

<<GPE_000022>>, <<GPE_000023>>
```

Let's have a look at the chatGPT response:

```txt
Subject: Invitation to <<EVENT_000018>> in <<GPE_000022>>

Dear Dr. <<PERSON_000019>>,

We invite you to attend <<EVENT_000018>> on <<DATE_000024>> in <<GPE_000022>>, <<GPE_000023>>. We're impressed by your research on climate change and carbon emissions' effects on the environment, particularly your recent paper on climate change's impact on marine ecosystems in <<ORG_000025>> <<DATE_000026>>.

As a leading expert, scientist, and policymaker in the field of climate change, we believe your insights would make a valuable contribution to the conference. This year's theme is "Innovative Solutions for a Sustainable Future," aligning with your research.

You'll have the opportunity to present your research, participate in workshops, attend panel discussions, and network with other experts in the field. Our keynote speaker is Dr. <<PERSON_000028>>, the director of <<ORG_000029>> at <<ORG_000030>>.

Please let us know if you're available to join us. We'd be delighted to provide you with further registration instructions and details.

Thank you for your time, and we look forward to your response.

Best regards,

<<PERSON_000020>>
Conference Coordinator
<<EVENT_000035>> in <<GPE_000022>>, <<GPE_000023>>
```

Copy the text into your clipboard and press F10. Then paste the result into your email program:

```txt
Subject: Invitation to the International Conference on Climate Change in Geneva

Dear Dr. James Smith,

We invite you to attend the International Conference on Climate Change on May 1-4, 2023 in Geneva, Switzerland. We're impressed by your research on climate change and carbon emissions' effects on the environment, particularly your recent paper on climate change's impact on marine ecosystems in the Journal of Environmental Science last year.

As a leading expert, scientist, and policymaker in the field of climate change, we believe your insights would make a valuable contribution to the conference. This year's theme is "Innovative Solutions for a Sustainable Future," aligning with your research.

You'll have the opportunity to present your research, participate in workshops, attend panel discussions, and network with other experts in the field. Our keynote speaker is Dr. Rajesh Sharma, the director of the Climate Change Division at the United Nations.

Please let us know if you're available to join us. We'd be delighted to provide you with further registration instructions and details.

Thank you for your time, and we look forward to your response.

Best regards,

Maria Perez
Conference Coordinator
International Conference on Climate Change in Geneva, Switzerland
```
