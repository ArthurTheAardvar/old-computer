yboard::isKeyPressed(sf::Keyboard::Space)) {
                pause = true;
            }
            if (sf::Keyboard::isKeyPressed(sf::Keyboard::LShift)) {
                pause = false;
            }

        }

        color = rc();
        //color = sf::Color::Green;

        window.clear(bgColor);

		for (int i = 0; i < 100000; i++) {
            if (pause == false) {
                pos = transform(image, color, pos);
            }
		}

		texture.loadFromImage(image);
		window.draw(fern);
window.display();
    }
}