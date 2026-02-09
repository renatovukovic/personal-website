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
      align-items: center;
      width: 100%; /* Ensure the clickable area covers the whole width */
      padding: 10px;
      color: var(--light-slate); /* Default text color */
      transition: var(--transition); /* Smooth transition for hover effects */

      &:hover,
      &:focus {
        color: var(--green); /* Change color on hover */
      }

      svg {
        width: 20px;
        height: 20px;
        margin-right: 10px; /* Space between icon and text */
      }

      span {
        font-size: var(--fz-xs); /* Font size for the name */
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
