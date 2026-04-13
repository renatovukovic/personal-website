import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';
import { Icon } from '@components/icons';
import { socialMedia, email } from '@config';

const StyledFooter = styled.footer`
  ${({ theme }) => theme.mixins.flexCenter};
  flex-direction: column;
  height: auto;
  min-height: 70px;
  padding: 15px;
  text-align: center;
`;

const StyledSocialLinks = styled.div`
  display: none;

  @media (max-width: 768px) {
    display: block;
    width: 100%;
    max-width: 270px;
    margin: 0 auto 10px;
    color: var(--light-slate);
  }

  ul {
    ${({ theme }) => theme.mixins.flexBetween};
    padding: 0;
    margin: 0;
    list-style: none;

    a {
      padding: 10px;
      svg {
        width: 20px;
        height: 20px;
      }
    }
  }
`;

const StyledCredit = styled.div`
  color: var(--light-slate);
  font-family: var(--font-mono);
  font-size: var(--fz-xxs);
  line-height: 1;

  a {
    padding: 10px;
  }

  .github-stats {
    margin-top: 10px;

    & > span {
      display: inline-flex;
      align-items: center;
      margin: 0 7px;
    }
    svg {
      display: inline-block;
      margin-right: 5px;
      width: 14px;
      height: 14px;
    }
  }
`;

const StyledLegalNotice = styled.div`
  color: var(--slate);
  font-family: var(--font-mono);
  font-size: var(--fz-xxs);
  line-height: 1.5;
  margin-top: 30px;
  max-width: 600px;
  border-top: 1px solid var(--lightest-navy);
  padding-top: 20px;

  .legal-section {
    margin-bottom: 15px;
  }

  .legal-title {
    font-weight: 600;
    color: var(--lightest-slate);
    margin-bottom: 5px;
    text-transform: uppercase;
    letter-spacing: 0.1em;
  }

  p {
    margin: 2px 0;
  }

  a {
    color: var(--green);
    &:hover {
      text-decoration: underline;
    }
  }
`;

const Footer = () => {
  const [githubInfo, setGitHubInfo] = useState({
    stars: null,
    forks: null,
  });

  useEffect(() => {
    if (process.env.NODE_ENV !== 'production') {
      return;
    }
    fetch('https://api.github.com/repos/bchiang7/v4')
      .then(response => response.json())
      .then(json => {
        const { stargazers_count, forks_count } = json;
        setGitHubInfo({
          stars: stargazers_count,
          forks: forks_count,
        });
      })
      .catch(e => console.error(e));
  }, []);

  return (
    <StyledFooter>
      <StyledSocialLinks>
        <ul>
          {socialMedia &&
            socialMedia.map(({ name, url }, i) => (
              <li key={i}>
                <a href={url} aria-label={name}>
                  <Icon name={name} />
                </a>
              </li>
            ))}
        </ul>
      </StyledSocialLinks>

      <StyledCredit tabindex="-1">
        <a href="https://github.com/bchiang7/v4">
          <div>Designed &amp; Built by Brittany Chiang</div>

          {githubInfo.stars && githubInfo.forks && (
            <div className="github-stats">
              <span>
                <Icon name="Star" />
                <span>{githubInfo.stars.toLocaleString()}</span>
              </span>
              <span>
                <Icon name="Fork" />
                <span>{githubInfo.forks.toLocaleString()}</span>
              </span>
            </div>
          )}
        </a>
      </StyledCredit>

      <StyledLegalNotice>
        <div className="legal-section">
          <div className="legal-title">Impressum</div>
          <p>Renato Sprenger-Vukovic</p>
          <p>Universitätsstraße 1</p>
          <p>40225 Düsseldorf</p>
          <p>
            E-Mail: <a href={`mailto:${email}`}>{email}</a>
          </p>
        </div>

        <div className="legal-section">
          <div className="legal-title">Legal Notice & GDPR</div>
          <p>
            This website complies with the Digital Services Act (DSA) and the General Data
            Protection Regulation (GDPR).
          </p>
          <p>
            <strong>Analytics:</strong> This website uses Google Analytics to analyze web traffic.
            Your IP address is anonymized before being stored. You can prevent the collection of
            your data by Google Analytics by using the{' '}
            <a
              href="https://tools.google.com/dlpage/gaoptout"
              target="_blank"
              rel="noopener noreferrer">
              Google Analytics Opt-out Browser Add-on
            </a>
            .
          </p>
          <p>
            You have the right to request information about your stored personal data, its origin,
            recipients, and the purpose of data processing at any time free of charge. You also have
            the right to request the correction, blocking, or deletion of this data.
          </p>
        </div>

        <div className="legal-section">
          <div className="legal-title">Disclaimer</div>
          <p>
            The contents of this website were created with the greatest care. However, I cannot
            guarantee the accuracy, completeness, or topicality of the content. As a service
            provider, I am responsible for my own content on these pages according to the general
            laws.
          </p>
        </div>
      </StyledLegalNotice>
    </StyledFooter>
  );
};

Footer.propTypes = {
  githubInfo: PropTypes.object,
};

export default Footer;
