from typing import List, NotRequired, TypedDict


class Text(TypedDict):
    type: str
    text: str


class Items(TypedDict):
    type: str


class OptionSelect(TypedDict):
    text: Text
    value: str


class OptionField(TypedDict):
    text: Text
    key: str
    type: str
    is_required: NotRequired[bool]
    options: NotRequired[List[OptionSelect]]
    items: NotRequired[Items]


DINO_TYPES = {
    "theropods": "A typical theropod dinosaur was bipedal, with strong hind legs for running and "
    "clawed hands for grasping prey. They often had sharp, serrated teeth for slicing meat, though "
    "some species adapted to herbivory or omnivory. Many were feathered and exhibited keen senses, "
    "such as sharp vision and smell, aiding their roles as agile hunters or opportunistic feeders.",
    "sauropods": "A typical sauropod dinosaur was massive, with a long neck for reaching high "
    "vegetation and a long tail for balance or defense. They walked on four sturdy, column-like "
    "legs and had small heads with peg-like teeth suited for stripping plants. Known for their "
    "enormous size, sauropods were gentle herbivores that traveled in herds and consumed vast "
    "amounts of vegetation daily.",
    "thyreophora": "A typical thyreophoran dinosaur was a heavily armored herbivore, protected by "
    "bony plates, spikes, or scutes embedded in their skin. They walked on four legs, with short, "
    "sturdy limbs and a low-slung body, feeding on low-growing plants. Examples like Stegosaurus "
    "had distinctive back plates and tail spikes, while ankylosaurs were built like living tanks "
    "with club-like tails for defense.",
    "stegosaurs": "A typical stegosaur dinosaur was a medium to large herbivore with a low-slung"
    "body, small head, and short forelimbs. It was characterized by double rows of large, upright "
    "plates along its back and spiked tails, likely used for defense. Stegosaurs primarily fed on "
    "low-growing vegetation and relied on their armored bodies to deter predators.",
    "ankylosauria": "A typical ankylosaur was a heavily armored herbivore with a low, wide body"
    "covered in bony plates and spikes for protection. It had a club-like tail that could be used "
    "as a powerful defensive weapon against predators. Ankylosaurs were quadrupedal, with strong, "
    "stocky legs and a beaked mouth for grazing on low-growing plants.",
    "ornithopods": "A typical ornithopod dinosaur was a herbivorous, bipedal or quadrupedal "
    "dinosaur with a beak and cheek teeth designed for grinding plants. They had strong, muscular "
    "hind limbs for running and often displayed a variety of adaptations for efficient feeding. "
    "Some species, like Iguanodon and Hadrosaurus, had large, duck-bill-like snouts and may have "
    "traveled in herds for protection.",
    "pachycephalosauria": "A typical pachycephalosaur was a small to medium-sized herbivorous "
    "dinosaur known for its thick, dome-shaped skull, which was likely used in head-butting "
    "behavior for defense or social interactions. They had relatively short limbs and bipedal "
    "posture, with a sturdy body built for stability. These dinosaurs may have lived in herds and "
    "used their domed skulls to compete for mates or territory.",
}
