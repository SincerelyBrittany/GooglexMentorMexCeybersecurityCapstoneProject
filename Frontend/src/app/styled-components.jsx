// styled-components.jsx
import styled from 'styled-components';

export const Container = styled.div`
  max-width: 600px;
  margin: 2rem auto;
  padding: 1.5rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
  background: #fff;
`;

export const Label = styled.label`
  display: block;
  margin: 1rem 0 0.5rem;
  font-weight: 500;
`;

export const Input = styled.input`
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-bottom: 1rem;
`;

export const Button = styled.button`
  padding: 0.5rem 1rem;
  background: #007BFF;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  &:hover {
    background: #0056b3;
  }
`;

export const Title = styled.h2`
  font-size: 1.5rem;
  margin-bottom: 1rem;
`;

export const Badge = styled.span`
  margin-left: 0.5rem;
  padding: 0.2rem 0.5rem;
  font-size: 0.75rem;
  background-color: #f8d7da;
  color: #721c24;
  border-radius: 12px;
`;

export const List = styled.ul`
  padding-left: 1.2rem;
`;

export const ListItem = styled.li`
  margin-bottom: 0.5rem;
  font-size: 1rem;
`;
