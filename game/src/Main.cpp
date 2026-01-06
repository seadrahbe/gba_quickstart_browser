#include <bn_backdrop.h>
#include <bn_core.h>
#include <bn_keypad.h>
#include <bn_sprite_ptr.h>

#include "bn_sprite_items_dot.h"

int main() {
    bn::core::init();

    bn::backdrop::set_color(bn::color(0, 0, 0));

    auto dot = bn::sprite_items::dot.create_sprite(0, 0);

    bn::fixed speed = 1.5;

    while(true) {
        if(bn::keypad::left_held()) {
            dot.set_x(dot.x() - speed);
        }
        if(bn::keypad::right_held()) {
            dot.set_x(dot.x() + speed);
        }
        if(bn::keypad::up_held()) {
            dot.set_y(dot.y() - speed);
        }
        if(bn::keypad::down_held()) {
            dot.set_y(dot.y() + speed);
        }
        bn::core::update();
    }
}