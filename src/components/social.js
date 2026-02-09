import React from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';
import { socialMedia } from '@config';
import { Side } from '@components';
import { Icon } from '@components/icons';

const StyledSocialList = styled.ul`
  display: flex;
  flex-direction: column;
  align-items: flex-start; /* Align items to the start for text */
  margin: 0;
  padding: 0;
  list-style: none;

  li {
    margin-bottom: 10px; /* Spacing between social links */

    &:last-of-type {
      margin-bottom: 0;
    }

    a {
      display: flex;
      flex-direction: column; /* Stack icon and text vertically */
      justify-content: flex-start; /* Left align content horizontally */
      align-items: flex-start; /* Left align content vertically */
      width: 100%;
      padding: 10px;
      color: var(--light-slate);
      transition: var(--transition);
      text-align: left; /* Left align text below the icon */

      &:hover,
      &:focus {
        color: var(--green);
      }

      svg {
        width: 20px;
        height: 20px;
        margin-right: 0; /* Remove horizontal margin */
        margin-bottom: 5px; /* Add vertical space between icon and text */
      }

      span {
        font-size: var(--fz-sm);
        color: var(--social-text-color);
      }
    }
  }
`;

const Social = ({ isHome }) => (
  <Side isHome={isHome} orientation="left">
    <StyledSocialList>
      {socialMedia &&
        socialMedia.map(({ url, name }, i) => (
          <li key={i}>
            <a href={url} aria-label={name} target="_blank" rel="noreferrer">
              <Icon name={name} />
              <span>{name}</span>
            </a>
          </li>
        ))}
    </StyledSocialList>
  </Side>
);

Social.propTypes = {
  isHome: PropTypes.bool,
};

export default Social;
